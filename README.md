# libpfm4PerformanceEventParser
A python parser to generate a JSON with all the different Events availables performance Events supported by libpfm4 in the OS. It uses as input the path to the **examples** folder in **libpfm4**.

The output JSON include the code value, names, PMU associated and descriptions of each Event and the multiple Umasks combinations.

# Usage

```./parser.py pathTo<./check_events>Fromlibpfm4```

the default output is to the stdout, but can be redirected to a file

```./parser.py pathTo<./check_events>Fromlibpfm4 > parsed.JSON```

# Example of output
```
{'IDX' : '106954793', 
'PMU name' : 'perf (perf_events generic PMU)', 
'Name' : 'PERF_COUNT_HW_CACHE_L1D', 
'Description' : 'L1 data cache', 
'Codes' : {'0x0': 'Umask-03 : 0x00 : PMU : [ACCESS] : None : hit access',
 '0x10000': 'Umask-00 : 0x00 : PMU : [READ] : None : read access; Umask-04 : 0x10000 : PMU : [MISS] : None : miss access',
 '0x10100': 'Umask-01 : 0x100 : PMU : [WRITE] : None : write access',
 '0x10200': 'Umask-02 : 0x200 : PMU : [PREFETCH] : None : prefetch access'} 
}
```
