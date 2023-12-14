#!/usr/bin/python3
import argparse,sys

sqli=[
    "id",
    "page",
    "dir",
    "search",
    "category",
    "file",
    "class",
    "url",
    "news",
    "item",
    "menu",
    "lang",
    "name",
    "ref",
    "title",
    "view",
    "topic",
    "thread",
    "type",
    "date",
    "form",
    "join",
    "main",
    "nav",
    "region"]

rce=[
    "cmd",
    "exec",
    "command",
    "execute",
    "ping",
    "query",
    "jump",
    "code",
    "reg",
    "do",
    "func",
    "arg",
    "option",
    "load",
    "process",
    "step",
    "read",
    "function",
    "req",
    "feature",
    "exe",
    "module",
    "payload",
    "run",
    "print"]

lfi=[
    "cat",
    "dir",
    "action",
    "board",
    "date",
    "detail",
    "file",
    "download",
    "path",
    "folder",
    "prefix",
    "include",
    "page",
    "inc",
    "locate",
    "show",
    "doc",
    "site",
    "type",
    "view",
    "content",
    "document",
    "layout",
    "mod",
    "conf"]

ssrf=[
    "dest",
    "redirect",
    "uri",
    "path",
    "continue",
    "url",
    "window",
    "next",
    "data",
    "reference",
    "site",
    "html",
    "val",
    "validate",
    "domain",
    "callback",
    "return",
    "page",
    "feed",
    "host",
    "port",
    "to",
    "out",
    "view",
    "dir"]

xss=[
    "q",
    "s",
    "search",
    "id",
    "lang",
    "keyword",
    "query",
    "page",
    "keywords",
    "year",
    "view",
    "email",
    "type",
    "name",
    "p",
    "month",
    "iamge",
    "list_type",
    "url",
    "terms",
    "categoryid",
    "key",
    "login",
    "begindate",
    "enddate"]

parser=argparse.ArgumentParser()
parser.add_argument("vuln",choices=["xss","sqli","rce","lfi","ssrf"])
parser.add_argument("replace_string")
args=parser.parse_args()

pattern=args.vuln
match pattern:
    case "sqli":
        vuln=sqli
    case "xss":
        vuln=xss
    case "rce":
        vuln=rce
    case "lfi":
        vuln=lfi
    case "ssrf":
        vuln=ssrf

url_input=sys.stdin.read().split("\n")
output=""
for line in url_input:
    params=[]
    try:
        params=line.split("?")[1].split("&")
    except:{}
    for p in params:
        for expected_param in vuln:
            if p.split("=")[0].lower()==expected_param:
                output+=line.replace(p,p.split("=")[0]+"="+args.replace_string)
                output+="\n"

print(output)