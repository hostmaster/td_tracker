# Reporting 

* track numbers of particular email newsletter opens with at least 1 hour granularity;

Newsletter id is 11
```SQL
SELECT uuid, timestamp, count(uuid) from clicks
WHERE uuid in (SELECT uuid FROM redirects WHERE letter_id == 11 and email is NULL)
AND timestamp >= datetime('now', '-1 hour')
```

* track numbers of particular URL "clicks" with at least 1 hour granularity;
```
SELECT uuid, timestamp, count(uuid) from clicks
WHERE uuid in (SELECT uuid FROM redirects WHERE url == 'http://goo.gl')
AND timestamp >= datetime('now', '-1 hour')
```

* track numbers of unique clicks of given URL with at least 1 hour granularity;
```
SELECT DISTINCT email from redirects
WHERE uuid in (SELECT uuid FROM clicks WHERE timestamp >= datetime('now', '-1 hour'))
AND url == 'http://goo.gl'
```

* answer the question "does user with email X followed an URL Y?"
```
SELECT url from redirects
WHERE uuid in (SELECT uuid from clicks)
AND email == 'n11u2@testdomain.tld'
```
