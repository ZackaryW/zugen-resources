
default_data("@/example-data/data.toml")
ensure_file("@/awesome-cv/awesome-cv.cls")
pandoc()
rename("pandoc.out", "resume.tex")
system("xelatex -interaction=nonstopmode resume.tex", throw=False)
capture("resume.pdf")