const fs = require('fs');
const readline = require('readline');
const crypto = require('crypto');

// key.js dosyasındaki anahtarın birebir aynısı olmalı!
const secretKey = 'furkan_camaro_2026_safe_data_32c'; 

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

console.clear();
let bins = [];

try {
    // 1. Şifreli datayı oku
    const content = fs.readFileSync('./encrypted.dat', 'utf8');
    const [ivHex, encryptedData] = content.split(':');
    
    // 2. Şifreyi çöz (Decryption)
    const decipher = crypto.createDecipheriv(
        'aes-256-cbc', 
        Buffer.from(secretKey), 
        Buffer.from(ivHex, 'hex')
    );
    
    let decrypted = decipher.update(encryptedData, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    
    // 3. Belleğe yükle
    bins = JSON.parse(decrypted);

    console.log("===============================================");
    console.log("     SECURE BIN SEARCH TOOL v1.0");
    console.log("===============================================");
    console.log(`[*] Secure Database Loaded: ${bins.length} records.`);
    console.log("[*] Type 'exit' to quit.");
    console.log("-----------------------------------------------");
} catch (err) {
    console.log("[!] ERROR: Access Denied or Data Corrupted.");
    process.exit(1);
}

const getBrand = (bin) => {
    const firstDigit = bin.toString()[0];
    if (firstDigit === '4') return 'VISA';
    if (['5', '2'].includes(firstDigit)) return 'MASTERCARD';
    if (['3'].includes(firstDigit)) return 'AMEX';
    if (firstDigit === '6') return 'DISCOVER/MAESTRO';
    return 'UNKNOWN';
};

const ask = () => {
    rl.question("\nEnter BIN or Card Number: ", (input) => {
        if (input.toLowerCase() === 'exit') {
            console.log("Exiting...");
            process.exit(0);
        }

        const cleanInput = input.trim();
        const matchedBin = bins.find(dbBin => cleanInput.startsWith(dbBin.toString().trim()));

        if (matchedBin) {
            console.log("\n>>> MATCH FOUND! <<<");
            console.log(`[+] BIN NUMBER : ${matchedBin}`);
            console.log(`[+] CARD BRAND : ${getBrand(matchedBin)}`);
            console.log(`[+] SOURCE     : Encrypted Database`);
            console.log("-----------------------------------------------");
        } else {
            console.log("\n[!] No match found in secure database.");
        }
        ask();
    });
};

ask();
