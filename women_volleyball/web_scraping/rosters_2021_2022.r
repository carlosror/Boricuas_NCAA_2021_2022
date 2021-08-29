ncaa_d1_colleges <- read.csv("NCAA_Division_1_volleyball_colleges_2019_2020.csv", stringsAsFactors = FALSE)
ncaa_d2_colleges <- read.csv("NCAA_Division_2_volleyball_colleges_2019_2020.csv", stringsAsFactors = FALSE)
ncaa_d3_colleges <- read.csv("NCAA_Division_3_volleyball_colleges_2019_2020.csv", stringsAsFactors = FALSE)
naia_colleges <- read.csv("NAIA_volleyball_colleges_2019_2020.csv", stringsAsFactors = FALSE)
njcaa_d1_colleges <- read.csv("NJCAA_Division_1_volleyball_colleges_2019_2020.csv", stringsAsFactors = FALSE)
ncjaa_d2_colleges <- read.csv("NJCAA_Division_2_volleyball_colleges_2019_2020.csv", stringsAsFactors = FALSE)

all_colleges_dfs <- list(ncaa_d1_colleges, ncaa_d2_colleges, ncaa_d3_colleges, naia_colleges, njcaa_d1_colleges, ncjaa_d2_colleges)

# lapply(all_colleges_dfs, function(college_df) {college_df$Roster = gsub("2019-20", "2021-22", college_df$Roster)})

for (i in 1:length(all_colleges_dfs)) {
  all_colleges_dfs[[i]]$Roster <- gsub("2019-20", "2021-22", all_colleges_dfs[[i]]$Roster)
  all_colleges_dfs[[i]]$Roster <- gsub("2019", "2021", all_colleges_dfs[[i]]$Roster)
  all_colleges_dfs[[i]]$Roster <- gsub("2020", "2022", all_colleges_dfs[[i]]$Roster)
}

write.csv(all_colleges_dfs[[1]], "NCAA_Division_1_volleyball_colleges_2021_2022.csv", row.names = FALSE)
write.csv(all_colleges_dfs[[2]], "NCAA_Division_2_volleyball_colleges_2021_2022.csv", row.names = FALSE)
write.csv(all_colleges_dfs[[3]], "NCAA_Division_3_volleyball_colleges_2021_2022.csv", row.names = FALSE)
write.csv(all_colleges_dfs[[4]], "NAIA_volleyball_colleges_2021_2022.csv", row.names = FALSE)
write.csv(all_colleges_dfs[[5]], "NJCAA_Division_1_volleyball_colleges_2021_2022.csv", row.names = FALSE)
write.csv(all_colleges_dfs[[6]], "NJCAA_Division_2_volleyball_colleges_2021_2022.csv", row.names = FALSE)