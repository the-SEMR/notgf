# NOTGF

As it indicates it is definitely not gf!!! (but best regards)

notgf is simple tool to grep input urls with intended parameters from tools like [waybackurls](https://github.com/tomnomnom/waybackurls) by the vulnerability and change the params one by one by the replacing string. 

Parameters used are from [Top-25 parameters](https://owasp.org/www-project-top-25-parameters/).

## Usage
Simply pipe in the output of mentioned tools, provide the vulnerability and intended replacing string. Outputs the the urls as a whole string divided by new line to stdout.
```bash
input_urls | python3 notgf.py {vulnerability} {replacing str} 
```
### example
```bash
$echo "https://example.com?id=xxx&dir=yyy&view=zzz" | python3 xss here
   
https://example.com?id=here&dir=yyy&view=zzz
https://example.com?id=xxx&dir=yyy&view=here

```
