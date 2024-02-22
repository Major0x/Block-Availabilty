const axios = require('axios'); // Import axios library for making HTTP requests

// Function to fetch blockchain project data
async function fetchBlockchainData() {
    try {
        // Make GET request to CoinGecko API to fetch blockchain data
        const response = await axios.get('https://api.coingecko.com/api/v3/coins/markets', {
            params: {
                vs_currency: 'usd', // Currency to compare
                ids: 'bitcoin,ethereum,cardano', // IDs of blockchain projects (Bitcoin, Ethereum, Cardano)
            },
        });

        // Extract data from the response
        const data = response.data;

        // Print project names and their respective current prices
        data.forEach(project => {
            console.log(`${project.name}: ${project.current_price} ${project.symbol.toUpperCase()}`);
        });
    } catch (error) {
        console.error('Error fetching blockchain data:', error.message);
    }
}

// Function to periodically fetch blockchain data
function checkBlockchainUptime(interval) {
    // Fetch blockchain data initially
    fetchBlockchainData();

    // Set interval to fetch blockchain data periodically
    setInterval(fetchBlockchainData, interval);
}

// Set the interval (in milliseconds) for fetching blockchain data (e.g., every 5 seconds)
const interval = 5000; // 5000 ms = 5 seconds

// Call the function to start checking blockchain uptime
checkBlockchainUptime(interval);
