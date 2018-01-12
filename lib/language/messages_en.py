#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    return \
        {
            "0": "Nettacker engine started ...\n\n",
            "1": "python nettacker.py [options]",
            "2": "Show Nettacker Help Menu",
            "3": "Please read license and agreements https://github.com/viraintel/OWASP-Nettacker\n",
            "4": "Engine",
            "5": "Engine input options",
            "6": "select a language {0}",
            "7": "scan all IPs in the range",
            "8": "find and scan subdomains",
            "9": "thread numbers for connections to a host",
            "10": "thread numbers for scan hosts",
            "11": "save all logs in file (results.txt, results.html, results.json)",
            "12": "Target",
            "13": "Target input options",
            "14": "target(s) list, separate with \",\"",
            "15": "read target(s) from file",
            "16": "Scan method options",
            "17": "choose scan method {0}",
            "18": "choose scan method to exclude {0}",
            "19": "username(s) list, separate with \",\"",
            "20": "read username(s) from file",
            "21": "password(s) list, separate with \",\"",
            "22": "read password(s) from file",
            "23": "port(s) list, separate with \",\"",
            "24": "read passwords(s) from file",
            "25": "time to sleep between each request",
            "26": "Cannot specify the target(s)",
            "27": "Cannot specify the target(s), unable to open file: {0}",
            "28": "it's better to use thread number lower than 100, BTW we are continuing...",
            "29": "set timeout to {0} seconds, it is too big, isn't it ? by the way we are continuing...",
            "30": "this scan module [{0}] not found!",
            "31": "this scan module [{0}] not found!",
            "32": "you cannot exclude all scan methods",
            "33": "you cannot exclude all scan methods",
            "34": "the {0} module you selected to exclude not found!",
            "35": "enter methods inputs, example: \"ftp_brute_users=test,admin&ftp_brute_passwds="
                  "read_from_file:/tmp/pass.txt&ftp_brute_port=21\"",
            "36": "cannot reading file {0}",
            "37": "Cannot specify the username(s), unable to open file: {0}",
            "38": "{0} found! ({1}:{2})",
            "39": "Cannot specify the password(s), unable to open file: {0}",
            "40": "file \"{0}\" is not writable!",
            "41": "please choose your scan method!",
            "42": "removing temp files!",
            "43": "sorting results!",
            "44": "done!",
            "45": "start attacking {0}, {1} of {2}",
            "46": "this module \"{0}\" is not available",
            "47": "unfortunately this version of the software just could be run on linux/osx/windows.",
            "48": "Your Python version is not supported!",
            "49": "skip duplicate target (some subdomains/domains may have same IP and Ranges)",
            "50": "unknown type of target [{0}]",
            "51": "checking {0} range ...",
            "52": "checking {0} ...",
            "53": "HOST",
            "54": "USERNAME",
            "55": "PASSWORD",
            "56": "PORT",
            "57": "TYPE",
            "58": "DESCRIPTION",
            "59": "verbose mode level (0-5) (default 0)",
            "60": "show software version",
            "61": "check for update",
            "62": "outgoing connections proxy (socks). example socks5: 127.0.0.1:9050, socks://127.0.0.1:9050,"
                  " socks5://127.0.0.1:9050 or socks4: socks4://127.0.0.1:9050, authentication: socks://username:"
                  "password@127.0.0.1, socks4://username:password@127.0.0.1, socks5://username:password@127.0.0.1",
            "63": "please enter valid socks address and port. example socks5: 127.0.0.1:9050, socks://127.0.0.1:9050,"
                  " socks5://127.0.0.1:9050 or socks4: socks4://127.0.0.1:9050, authentication: socks://username:passwo"
                  "rd@127.0.0.1, socks4://username:password@127.0.0.1, socks5://username:password@127.0.0.1",
            "64": "Retries when the connection timeout (default 3)",
            "65": "ftp connection to {0}:{1} timeout, skipping {2}:{3}",
            "66": "LOGGED IN SUCCESSFULLY!",
            "67": "LOGGED IN SUCCESSFULLY, PERMISSION DENIED FOR LIST COMMAND!",
            "68": "ftp connection to {0}:{1} failed, skipping whole step [process {2} of {3}]! going to next step",
            "69": "input target for {0} module must be DOMAIN, HTTP or SINGLE_IPv4, skipping {1}",
            "70": "user: {0} pass:{1} host:{2} port:{3} found!",
            "71": "(NO PERMISSION FOR LIST FILES)",
            "72": "trying {0} of {1} in process {2} of {3} {4}:{5}",
            "73": "smtp connection to {0}:{1} timeout, skipping {2}:{3}",
            "74": "smtp connection to {0}:{1} failed, skipping whole step [process {2} of {3}]! going to next step",
            "75": "input target for {0} module must be HTTP, skipping {1}",
            "76": "ssh connection to {0}:{1} timeout, skipping {2}:{3}",
            "77": "ssh connection to {0}:{1} failed, skipping whole step [process {2} of {3}]! going to next step",
            "78": "ssh connection to %s:%s failed, skipping whole step [process %s of %s]! going to next step",
            "79": "OPEN PORT",
            "80": "host: {0} port: {1} found!",
            "81": "target {0} submitted!",
            "82": "cannot open proxies list file: {0}",
            "83": "cannot find proxies list file: {0}",
            "84": "you are running OWASP Nettacker version {0}{1}{2}{6} with code name {3}{4}{5}",
            "85": "this feature is not available yet! please run \"git clone https://github.com/viraintel/OWAS"
                  "P-Nettacker.git\" or \"pip install -U OWASP-Nettacker\" to get the last version.",
            "86": "build a graph of all activities and information, you must use HTML output. available graphs: {0}",
            "87": "to use graph feature your output filename must end with \".html\" or \".htm\"!",
            "88": "building graph ...",
            "89": "finish building graph!",
            "90": "Penetration Testing Graphs",
            "91": "This graph created by OWASP Nettacker. Graph contains all modules activities, network map and"
                  " sensitive information, Please don't share this file with anyone if it's not reliable.",
            "92": "OWASP Nettacker Report",
            "93": "Software Details: OWASP Nettacker version {0} [{1}] in {2}",
            "94": "no open ports found!",
            "95": "no user/password found!",
            "96": "{0} modules loaded ...",
            "97": "this graph module not found: {0}",
            "98": "this graph module \"{0}\" is not available",
            "99": "ping before scan the host",
            "100": "skipping whole target {0} and scanning method {1} because of --ping-before-scan is true and "
                   "it didn't response!",
            "101": "you are not using the last version of OWASP Nettacker, please update.",
            "102": "cannot check for update, please check your internet connection.",
            "103": "You are using the last version of OWASP Nettacker ...",
            "104": "directoy listing found in {0}",
            "105": "please insert port through the -g or --methods-args switch instead of url",
            "106": "http connection {0} timeout!",
            "107": "",
            "108": "no directory or file found for {0} in port {1}",
            "109": "unable to open {0}",
            "110": "dir_scan_http_method value must be GET or HEAD, set default to GET.",
            "111": "list all methods args",
            "112": "cannot get {0} module args",
            "113": "trying {0} of {1} in process {2} of {3} on {4} (viewdns ip lookup)",
            "114": "{0} domain found: {1}",
            "115": "TIME",
            "116": "CATEGORY",
            "117": "cannot find any module with {0} pattern!"
        }
