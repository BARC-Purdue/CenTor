## ARTIFACT EVALUATION:
* Open 4 terminals on reviewer A account on Bento. 
* Run tor on first. 
* On the second terminal, start the Bento Server using `cd Bento/bento/server` and `sudo ./runserver.py`. 
* On the third terminal, connect the client to the Bento Server and upload and run the `centor.func` using `cd Bento/testing/CenTor` and `python3 bento_driver.py 0.0.0.0 8888`. 
* On the fourth terminal, connect to the Bento Server and transfer the service files to the server using `cd Bento/testing/CenTor/setup` and `python3 client_ftp.py`.(sample input: `1, test, test/, index.html`)

## DEBUG
1. Check the configuration files `/etc/apache2/sites-available/test.conf` and `/etc/apache2/apache2.conf`. 
2. Check the `centor.func` for its folder creation directory.
3. Reload apache using ` sudo systemctl restart apache2`. 
4. Run server script with `sudo`.
5. Remove `test` in `/tmp/` using `sudo rm -r /temp/test` in case of hostname or key error. 

## APACHE 

1. Root directory for website files: /etc/apache2/apache2.conf
2. Website config files: /etc/apache2/sites-available/sites-available/test.conf

## HIDDEN SERVICE
1. Folder that stores hostname and keys: /tmp/test/


[Reference](https://www.liquidweb.com/kb/configure-apache-virtual-hosts-ubuntu-18-04/)

(PVT NOTES
Tested on SGX on reva; set torrc to non-anon; client scripts run on virginia; normal HS on oregon;)
