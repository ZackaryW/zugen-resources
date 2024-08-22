default_data("@/example-data/old.toml")
pandoc()
rename("pandoc.out", "resume.md")
capture("resume.md")
