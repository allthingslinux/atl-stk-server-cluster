# SuperTuxKart Server Cluster with NGINX Load Balancing

This project sets up a cluster of SuperTuxKart servers with NGINX as a load balancer using Docker Compose. It includes secure handling of login credentials using Docker secrets.

## Prerequisites

- Docker
- Docker Compose
- sqlite3

## Setup

### Step 1: Create Docker Secrets

First, create Docker secrets for your SuperTuxKart login credentials. Replace `your_login` and `your_password` with your actual SuperTuxKart login and password.

```bash
echo "your_login" | docker secret create stk_login -
echo "your_password" | docker secret create stk_password -
```

### Step 2: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/allthingslinux/atl-stk-loadhandler
cd atl-stk-loadhandler
```

### Step 3: Prepare `bans.db`

This file is the database for banned users. Run the following commands to set it up:

```bash
sqlite3 bans.db "CREATE TABLE IF NOT EXISTS bans (id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE);"
```

### Step 4: Configuration

#### ✦ NGINX Configuration

The NGINX container uses the configuration specified in `dockerfile.nginx`. It is set up for round-robin load balancing across the three SuperTuxKart servers.

#### ✦ Docker Compose File

The `docker-compose.yml` file includes the definitions for the SuperTuxKart servers and the NGINX load balancer. You can modify this file to adjust port mappings and other settings.

#### ✦ SuperTuxKart Server Configuration

The SuperTuxKart servers are configured using the `server_config.xml` file. You can modify this file to change the server settings as needed.

### Step 5: Build and Run the Containers

Use Docker Compose to build the containers:

```bash
docker-compose build
```

This will build the images and start three SuperTuxKart servers along with an NGINX container for load balancing.

### Step 6: Starting the Servers

Start the servers using Docker Compose:

```bash
docker-compose up -d
```

### Step 7: Accessing the Servers

After starting the containers, the SuperTuxKart servers will be accessible on the following ports:

- `stk-server1`: `http://localhost:5001`
- `stk-server2`: `http://localhost:5002`
- `stk-server3`: `http://localhost:5003`

NGINX will balance the load across these servers on port `2759`:

- `NGINX Load Balancer`: `http://localhost:2759`

### Step 8: Stopping the Containers

To stop the containers, use the following command:

```bash
docker-compose down
```

This will stop and remove the containers while preserving the Docker secrets.

## Troubleshooting

- **Build Failures**: Ensure that all necessary dependencies are installed and that the Docker secrets are correctly created.
- **Configuration Issues**: Verify that the `server_config.xml` and `bans.db` files are correctly placed and formatted.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please create a pull request or open an issue to discuss any changes or improvements.

## Contact

For any questions or support, please contact `@tyttggfdsddgh` in the https://discord.gg/linux via a ticket, which you can create with the `/ticket` command in any channel of the server.

