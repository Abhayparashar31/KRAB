<%*
// ========================================
// KRAB MITRE TTP CORRELATION ENGINE ONLY
// ========================================

const file = app.workspace.getActiveFile();
if (!file) {
    new Notice("❌ No active file detected!");
    return;
}

// Identify the entity type of the current active file
const currentPath = file.path;
let sourceType = "";
if (currentPath.startsWith("01_Threat_Actor")) sourceType = "actor";
else if (currentPath.startsWith("03_Campaigns")) sourceType = "campaign";
else if (currentPath.startsWith("04_Malware")) sourceType = "malware";
else if (currentPath.startsWith("05_Vulnerabilities")) sourceType = "vulnerability";

// If the file being evaluated isn't one of your primary threat pillars, halt.
if (sourceType === "") {
    new Notice("ℹ️ Skipped: Active note is not inside an actor, campaign, malware, or vulnerability folder.");
    return;
}

const cache = app.metadataCache.getFileCache(file);
const links = cache?.links || [];

if (links.length === 0) {
    new Notice("⚠️ No internal links found in this note.");
    return;
}

const ttpUpdateQueue = [];

// ========================================
// 1. FILTER AND ISOLATE ONLY TTP LINKS
// ========================================
for (const link of links) {
    const linkPath = link.link;
    if (!linkPath) continue;

    // Route strictly and exclusively links inside the 02_TTPs folder
    if (linkPath.startsWith("02_TTPs/")) {
        if (!ttpUpdateQueue.includes(linkPath)) {
            ttpUpdateQueue.push(linkPath);
        }
    }
}

if (ttpUpdateQueue.length === 0) {
    new Notice("ℹ️ No links to '02_TTPs' discovered in this file.");
    return;
}

// ========================================
// 2. EXECUTION ENGINE: BACKLINK MITRE TTPs
// ========================================
let updatedTtpCount = 0;

for (const linkPath of ttpUpdateQueue) {
    const targetFilePath = linkPath.endsWith(".md") ? linkPath : `${linkPath}.md`;
    const tpFile = app.vault.getAbstractFileByPath(targetFilePath);
    
    // Skip if the scraped MITRE TTP note doesn't exist in your vault yet
    if (!tpFile) continue; 

    const content = await app.vault.read(tpFile);
    
    // Prevent duplicate injection tracking lines
    if (!content.includes(`[[${file.basename}]]`)) {
        let appendText = "";
        if (!content.includes("### 🔗 KRAB Intelligence Correlation")) {
            appendText += "\n\n### 🔗 KRAB Intelligence Correlation\n";
        }
        
        // Inject distinct lineage tracking strings with precise inline Dataview keys
        if (sourceType === "actor") {
            appendText += `- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[${file.basename}]] [related_actor:: [[${file.basename}]]]\n`;
        } else if (sourceType === "campaign") {
            appendText += `- ⚔️ **Active Operation Deployment:** Tracked in campaign [[${file.basename}]] [related_campaign:: [[${file.basename}]]]\n`;
        } else if (sourceType === "malware") {
            appendText += `- 🦠 **Tooling Capability Integration:** Executed via malware family [[${file.basename}]] [related_malware:: [[${file.basename}]]]\n`;
        } else if (sourceType === "vulnerability") {
            appendText += `- 🔓 **Exploitation Context:** Exploited alongside [[${file.basename}]] [related_vuln:: [[${file.basename}]]]\n`;
        }
        
        if (appendText !== "") {
            await app.vault.append(tpFile, appendText);
            updatedTtpCount++;
        }
    }
}

// Final user notifications
if (updatedTtpCount > 0) {
    new Notice(`🎉 Ingestion Complete! Correlated ${updatedTtpCount} MITRE TTP notes seamlessly.`);
} else {
    new Notice("✅ Clean run: All linked TTPs already carry up-to-date relationship records.");
}
-%>