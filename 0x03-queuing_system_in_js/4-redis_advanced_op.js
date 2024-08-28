// Import the redis library using ES6 syntax
import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Function to store hash values in Redis
function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);
}

// Function to display the hash values stored in Redis
function displayHash() {
  client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
      console.error('Error retrieving hash:', err);
    } else {
      console.log(result);
    }
  });
}

// Call the functions to create and display the hash
createHash();
displayHash();
