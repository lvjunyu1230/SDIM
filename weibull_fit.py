import weibull


x = [76,77,75,75,63,71,74,54,66,76,69,69,65,54,68,75,58,74,58,65,78,70,53,58,55,66,73,66,63,79,70,72,86,72,68,72,65,75]
# this is where the actual analysis and curve fitting occur
# analysis = weibull.Analysis(fail_times, unit='hour')
analysis = weibull.Analysis(x, unit='hour')
analysis.fit()

analysis.probplot(file_name='weibull-fit-10pt.png')
# analysis.hazard(file_name='hazard.png')
analysis.pdf(file_name='pdf.png')
analysis.cdf(file_name='cdf.png')
print(analysis.stats)
