default_data("@/example-data/data.toml")
pandoc()
rename("pandoc.out", "resume.md")
capture("resume.md")
