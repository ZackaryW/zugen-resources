---
title: "$info.firstname$ $info.lastname$ - Résumé"
date: \today
---

# $info.firstname$ $info.lastname$

**Position:** $for(profile.corecomp)$profile.corecomp${\enskip\cdotp\enskip}$endfor$

$if(info.address)$
**Address:** $info.address$
$else$
**Address:** $info.street$  
$info.city$, $info.province$  
$info.country$  
$info.postalcode$
$endif$

**Mobile:** $info.mobile$  
**Email:** $info.email$  
$if(info.homepage)$
**Homepage:** [$info.homepage$]($info.homepage$)
$endif$
$if(info.github)$
**GitHub:** [$info.github$]($info.github$)
$endif$
$if(info.gitlab)$
**GitLab:** $info.gitlab$
$endif$
$if(info.linkedin)$
**LinkedIn:** $info.linkedin$
$endif$

---

## Summary

$profile.summary$

---

## Qualifications

$if(profile.topqual)$
$for(profile.topqual)$
- $profile.topqual$
$endfor$
$endif$

$if(qual)$
$for(qual)$
### $qual.title$

$for(qual.items)$
- $qual.items$
$endfor$
$endfor$
$endif$

---

## Work Experience

$for(exp)$
### $exp.position$ at $exp.organization$

**Location:** $exp.location$  
**Dates:** $exp.datestart$ - $exp.dateend$

$if(exp.items)$
$for(exp.items)$
- $exp.items$
$endfor$
$endif$
$endfor$

$if(expl)$
$for(expl)$
### $expl.title$

$for(expl.items)$
$expl.items.name$  
$expl.items.des$  
$expl.items.location$  
$expl.items.year$
$endfor$
$endfor$
$endif$

---

## Projects

$if(project)$
$for(project)$
### $project.name$

**Type:** $project.type$  
**Position:** $project.position$  
**Dates:** $project.datestart$ - $project.dateend$

$if(project.items)$
$for(project.items)$
- $project.items$
$endfor$
$endif$
$endfor$
$endif$

$if(projectl)$
### Other Notable Projects

$for(projectl.items)$
#### $projectl.title$

$for(projectl.items)$
$projectl.items.name$  
$projectl.items.des$  
$projectl.items.location$  
$projectl.items.year$
$endfor$
$endfor$
$endif$

---

## Other Experience

$if(otherexp)$
$for(otherexp)$
### $otherexp.position$ at $otherexp.organization$

**Location:** $otherexp.location$  
**Dates:** $otherexp.datestart$ - $otherexp.dateend$

$if(otherexp.items)$
$for(otherexp.items)$
- $otherexp.items$
$endfor$
$endif$
$endfor$
$endif$

$if(otherexpl)$
$for(otherexpl)$
### $otherexpl.title$

$for(otherexpl.items)$
$otherexpl.items.name$  
$otherexpl.items.des$  
$otherexpl.items.location$  
$otherexpl.items.year$
$endfor$
$endfor$
$endif$

---

## Education

$for(edu)$
### $edu.degree$ at $edu.institution$

**Location:** $edu.location$  
**Dates:** $edu.datestart$ - $edu.dateend$

$if(edu.items)$
$for(edu.items)$
- $edu.items$
$endfor$
$endif$
$endfor$

$if(edul)$
$for(edul)$
### $edul.title$

$for(edul.items)$
$edul.items.name$  
$edul.items.des$  
$edul.items.location$  
$edul.items.year$
$endfor$
$endfor$
$endif$
