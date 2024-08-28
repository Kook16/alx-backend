import { createClient, print } from 'redis';
import { promisify } from 'util';

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

// Promisify the client.get function
const getAsync = promisify(client.get).bind(client);

// Function to set a new school in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // Use redis.print to display a confirmation message
}

// Async function to display the value of a school in Redis
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (err) {
    console.error('Error retrieving data:', err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
