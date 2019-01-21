#! /usr/bin/env python3
import sys

if len(sys.argv) > 3:
  ra_degrees = float(sys.argv[1]) * 15.0
  ra_mins_as_secs = float(sys.argv[2])*60
  ra_total_secs = ra_mins_as_secs + float(sys.argv[3])
  ra_frac_degree = ra_degrees + ra_total_secs / 3600
  print("RA: {}H {}M {}S => {} degrees".format(ra_degrees, sys.argv[2], sys.argv[3], ra_frac_degree))
  if len(sys.argv) > 6:
    dec_degrees = float(sys.argv[4])
    dec_mins_as_secs = float(sys.argv[5])*60
    dec_total_secs = dec_mins_as_secs + float(sys.argv[6])
    dec_frac_degree = dec_degrees + dec_total_secs/3600
    print("Dec: {}º {}' {}\" => {} degrees".format(sys.argv[4], sys.argv[5], sys.argv[6], dec_frac_degree))
else:
  print("Expected 3 Arguments: [Hours] [Minutes] [Seconds]")
print("finished") 