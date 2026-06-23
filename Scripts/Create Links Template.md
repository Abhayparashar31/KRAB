<%*
// ========================================
// NOTE AUTO-CREATION RUNTIME (PRE-FLIGHT CHECK)
// ========================================

const ALLOWED_FOLDERS = [
    "01_Threat_Actors",
    "03_Campaigns",
    "04_Malware",
    "05_Vulnerabilities"
];

const PLACEHOLDERS = ["ActorName", "CampaignName", "MalwareName", "CVE-XXXX-XXXX"];
const MINIMUM_CVE_YEAR = 2021;

const file = app.workspace.getActiveFile();
if (!file) {
    new Notice("❌ No active file detected!");
    return;
}

const cache = app.metadataCache.getFileCache(file);
const links = cache?.links || [];

if (links.length === 0) {
    new Notice("⚠️ No internal links found in this note.");
    return;
}

// ========================================
// 1. PRE-FLIGHT VALIDATION QUEUE
// ========================================
const creationQueue = [];

for (const link of links) {
    const linkPath = link.link;
    
    // Safety filters
    if (!linkPath || !linkPath.includes("/")) continue;
    if (PLACEHOLDERS.some(p => linkPath.includes(p))) continue;

    const topFolder = linkPath.split('/')[0];
    if (!ALLOWED_FOLDERS.includes(topFolder)) continue;

    // Stale CVE filter
    const cveMatch = linkPath.match(/CVE-(\d{4})-\d+/i);
    if (cveMatch) {
        const cveYear = parseInt(cveMatch[1], 10);
        if (cveYear < MINIMUM_CVE_YEAR) continue; 
    }
    
    const targetFilePath = linkPath.endsWith(".md") ? linkPath : `${linkPath}.md`;
    const abstractFile = app.vault.getAbstractFileByPath(targetFilePath);
    
    // Skip if file already exists
    if (abstractFile) continue;

    // If it passes all rules, add it to our confirmed queue
    creationQueue.push({
        targetFilePath,
        noteTitle: linkPath.split('/').pop(),
        folderPath: linkPath.substring(0, linkPath.lastIndexOf('/'))
    });
}

// ========================================
// 2. EXECUTION ENGINE (Only runs if items exist)
// ========================================
if (creationQueue.length === 0) {
    new Notice("✅ Clean run: No new valid intel notes needed to be created.");
    return; // Exits cleanly without touching the vault
}

new Notice(`📂 Processing queue: Creating ${creationQueue.length} missing notes...`);
let createdCount = 0;

for (const item of creationQueue) {
    // Securely build directories if missing
    if (item.folderPath && !(await app.vault.adapter.exists(item.folderPath))) {
        await app.vault.createFolder(item.folderPath);
    }

    // Set up standard target stub content
    const basicContent = `#### Created automatically from backlink in [[${file.basename}]].`;

    // Commit file creation to disk
    await app.vault.create(item.targetFilePath, basicContent);
    createdCount++;
    console.log(`Created vetted intel stub: ${item.targetFilePath}`);
}

new Notice(`🎉 Successfully created ${createdCount} valid intel notes!`);
-%>