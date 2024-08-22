
default_data("@/example-data/old.toml")
ensure_file("@/awesome-cv/modified.cls")
rename("modified.cls", "awesome-cv.cls")
pandoc()
rename("pandoc.out", "resume.tex")
system("xelatex -interaction=nonstopmode resume.tex")
capture("resume.pdf")