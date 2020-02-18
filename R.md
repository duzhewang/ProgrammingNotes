- This R command lists all packages installed by the user and the package versions.
```
ip <- as.data.frame(installed.packages()[,c(1,3:4)])
rownames(ip) <- NULL
ip <- ip[is.na(ip$Priority),1:2,drop=FALSE]
print(ip, row.names=FALSE)
```
- R package book: http://r-pkgs.had.co.nz/
