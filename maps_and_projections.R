
rm(list=ls())

library(sp)
library(rgdal)
library(geosphere)
library(tidyverse)

#clustering points
df = as_tibble(read.csv("C:/Users/stuar/Documents/GitHub/Bright_spot/Inverts_DB/Echinoderm_ave.csv", stringsAsFactors = F))
?c

x <- c(df$Lon)
y <- c(df$Lat)

# convert data to a SpatialPointsDataFrame object
xy <- SpatialPointsDataFrame(
  matrix(c(x,y), ncol=2), data.frame(ID=seq(1:length(x))),
  proj4string=CRS("+proj=longlat +ellps=WGS84 +datum=WGS84"))

# use the distm function to generate a geodesic distance matrix in meters
mdist <- distm(xy)

# cluster all points using a hierarchical clustering approach
hc <- hclust(as.dist(mdist), method="complete")

# define the distance threshold, in this case 40 m
d=4500

# define clusters based on a tree "height" cutoff "d" and add them to the SpDataFrame
xy$clust <- cutree(hc, h=d)

write.csv(xy,"C:/Users/stuar/Documents/GitHub/Bright_spot/Inverts_DB//Echinoderm_cluster.csv", row.names = FALSE)
