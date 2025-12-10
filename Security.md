## Overview
This repository uses 3 types of scanning, DAST, SAST and SCA

## SAST (Static analysis with CodeQL)
# What it does
Analyse source code for vulnerabilities
Detects programming flaws and insecure coding patterns
Provides data-flow and taint analysis

# When it runs
Every pull and push to the main branch
On weekly scheduled runs if configurated

# Checks for
Injection vulnerabilities (SQL injection, command injection)
Path traversal
Insecure deserialization
Use of dangerous APIs
Hardcoded secrets
Authentication/authorization logic issues
Memory safety issues (if applicable)

# Artifacts
CodeQL results
Sarif report

## SCA (Dependency Check)
# What it does
Scans Python dependencies for known CVEs
Checks for vulnerable library versions
Reports dependency metadata and severity scores

# When it runs
On push to main
On pull request
Manual workflow dispatch

# Checks for
Outdated or vulnerable libraries
Known CVEs from:
NVD (National Vulnerability Database)
OSS Index
GitHub Advisory Database
Dependency metadata and integrity

# Artifacts
- sca-reports ZIP containing:
dependency-check-report.json
dependency-check-report.xml
dependency-check-report.sarif
HTML & CSV reports

## DAST (Dynamic Analysis with OWASP ZAP)
# What it does
Tests the running application for security vulnerabilities
Executes HTTP-based attacks against your endpoints
Checks server headers, runtime misconfigurations, and exposed metadata

# When it runs
On push to main
On pull request
After application build & startup inside CI

# Checks for
Missing security headers
(e.g., X-Frame-Options, Cache-Control, Permissions-Policy)
Server version leakage
Runtime configuration issues
Unrestricted access to sensitive endpoints
Authentication issues (if applicable)
API/HTTP misconfigurations

# Artifacts
zap-baseline-reports
zap-fullscan-reports
# Each include:
JSON report
HTML report
Markdown summary

## Understanding Results
Please refer to:

Part 10: https://github.com/NewCOder10000/calculator-security-demo/actions/runs/20095442985

## Reporing vulnerabilities
Please email S10257575@connect.np.edu.sg


