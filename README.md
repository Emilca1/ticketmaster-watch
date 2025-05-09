# ticketmaster-watch

Allow to scan a website page to detect change and alert by email. Used for ticketmaster to alert when advance ticket sales is open

# Installation

Used with python venv

Install python
```
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
```

Create venv
```
python3 -m venv ticketmaster-watch
source ticketmaster-watch/bin/activate
```

Install dependances
```
pip install requests beautifulsoup4
```

create the watcher.py file
```
cd ticketmaster-watcher
nano watcher.py
```

Test it
```
source ticketmaster-watch/bin/activate
python watcher.py
```


If you want to automate it
```
crontab -e
*/10 * * * * /srv/ticketmaster-watcher/bin/python /srv/ticketmaster-watcher/watcher.py
```