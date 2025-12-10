## Findings

Code    Issue                               Risk    Affected                                                              Why it matters
10020   Missing anti click-jacking header   Medium  Localhost:5000                                                        Prevents click-jacking attacks
10036   Server leaks version Information    Low     Localhost:5000                                                        Prevents fingerprint attacks
10048   Cache control header missing        Low     Localhost:5000, /robots.txt, /favicon.ico, /feed.xml, /sitemap.xml    Prevents sensitive data being stored by browsers      
