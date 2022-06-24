# Installation on Raspberry Pie (Fresh Raspi 4)

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y git python3-venv
git clone https://github.com/codepals-org/hackathon-servus-zukunft.git
python3 -m venv .venv
source .venv/bin/activate
```

# Credentials needed to run the Python script

Create a file .env and place your MongoDB credentials there...

    MONGODB_URI=mongodb+srv://<user>:<password>@<host>/?retryWrites=true&w=majority

Never put your credentials in a public repository, so keep this .env out of your repo.

