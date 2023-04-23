import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt


# Read the data from the web page
data = '''\
1880     -0.17     -0.10
1881     -0.09     -0.13
1882     -0.11     -0.17
1883     -0.18     -0.21
1884     -0.28     -0.24
1885     -0.33     -0.27
1886     -0.32     -0.27
1887     -0.37     -0.28
1888     -0.18     -0.27
1889     -0.11     -0.26
1890     -0.35     -0.26
1891     -0.23     -0.26
1892     -0.27     -0.27
1893     -0.31     -0.26
1894     -0.30     -0.24
1895     -0.23     -0.22
1896     -0.11     -0.21
1897     -0.11     -0.18
1898     -0.28     -0.17
1899     -0.18     -0.17
1900     -0.08     -0.20
1901     -0.15     -0.23
1902     -0.28     -0.26
1903     -0.37     -0.28
1904     -0.47     -0.31
1905     -0.26     -0.34
1906     -0.22     -0.36
1907     -0.39     -0.37
1908     -0.43     -0.39
1909     -0.49     -0.41
1910     -0.43     -0.41
1911     -0.44     -0.39
1912     -0.36     -0.35
1913     -0.34     -0.32
1914     -0.15     -0.31
1915     -0.14     -0.30
1916     -0.36     -0.29
1917     -0.46     -0.29
1918     -0.29     -0.30
1919     -0.27     -0.29
1920     -0.27     -0.27
1921     -0.18     -0.26
1922     -0.28     -0.25
1923     -0.26     -0.24
1924     -0.27     -0.23
1925     -0.22     -0.22
1926     -0.10     -0.21
1927     -0.21     -0.20
1928     -0.19     -0.19
1929     -0.36     -0.18
1930     -0.15     -0.18
1931     -0.09     -0.18
1932     -0.15     -0.17
1933     -0.28     -0.16
1934     -0.12     -0.15
1935     -0.19     -0.13
1936     -0.14     -0.10
1937     -0.02     -0.06
1938      0.00     -0.01
1939     -0.02      0.03
1940      0.13      0.07
1941      0.19      0.09
1942      0.07      0.11
1943      0.09      0.10
1944      0.20      0.08
1945      0.09      0.04
1946     -0.07      0.01
1947     -0.02     -0.03
1948     -0.10     -0.07
1949     -0.11     -0.08
1950     -0.17     -0.07
1951     -0.07     -0.07
1952      0.01     -0.07
1953      0.08     -0.07
1954     -0.13     -0.07
1955     -0.14     -0.06
1956     -0.19     -0.05
1957      0.05     -0.04
1958      0.06     -0.01
1959      0.03      0.01
1960     -0.03      0.03
1961      0.06      0.01
1962      0.03     -0.01
1963      0.05     -0.03
1964     -0.20     -0.04
1965     -0.11     -0.05
1966     -0.06     -0.06
1967     -0.02     -0.05
1968     -0.08     -0.03
1969      0.05     -0.02
1970      0.03     -0.00
1971     -0.08      0.00
1972      0.01      0.00
1973      0.16     -0.00
1974     -0.07      0.01
1975     -0.01      0.02
1976     -0.10      0.04
1977      0.18      0.07
1978      0.07      0.12
1979      0.16      0.16
1980      0.26      0.20
1981      0.32      0.21
1982      0.14      0.22
1983      0.31      0.21
1984      0.16      0.21
1985      0.12      0.22
1986      0.18      0.24
1987      0.32      0.27
1988      0.39      0.31
1989      0.27      0.33
1990      0.45      0.33
1991      0.40      0.33
1992      0.22      0.33
1993      0.23      0.33
1994      0.32      0.34
1995      0.45      0.37
1996      0.33      0.40
1997      0.46      0.42
1998      0.61      0.44
1999      0.38      0.47
2000      0.39      0.50
2001      0.54      0.52
2002      0.63      0.55
2003      0.62      0.58
2004      0.53      0.61
2005      0.68      0.62
2006      0.64      0.62
2007      0.66      0.63
2008      0.54      0.64
2009      0.66      0.64
2010      0.72      0.65
2011      0.61      0.67
2012      0.65      0.70
2013      0.68      0.74
2014      0.75      0.79
2015      0.90      0.83
2016      1.02      0.88
2017      0.92      0.91
2018      0.85      0.93
2019      0.98      0.92
2020      1.02      0.92
2021      0.85      0.91
2022      0.89      0.90
'''

# Read the data into a pandas DataFrame
df = pd.read_csv(io.StringIO(data), sep='\s+',header=None, names=['Year','raw','smooth'])

sns.lineplot(x='Year', y='raw', data=df, label='Raw')
plt.title("Temperature Above Average")
plt.show()
