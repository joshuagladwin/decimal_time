# Decimal Time

Because I'm a sci-fi geek who loves a good [stardate](https://en.wikipedia.org/wiki/Stardate), I implemented a decimal datetime clock and to sit on my desktop.\
\
Is the code a little messy? Probably. Is it actually a useful/good way of tracking time and dates? Probably not. Ultimately, it's just a silly little fun program to give me a stardate-like measure of time and date. _Two-Three-Nine-Three-Two-Point-Four_...\
\
The `.pyw` version allows it to be run without opening a terminal window on Windows.

![Screenshot showing the decimal clock at datetime 23932.44793 next to the standard Windows clock, showing 10:45 06/12/2023](/img/example.png)

The Date and Time components are split by `.`. The format is as follows: 
>YYMDD.HMMSS

## Time

The time component is a simple implement of [decimal time](https://en.wikipedia.org/wiki/Decimal_time), where a day is split into 10 hours, each hour comprised of 100 minutes and each minute 100 seconds. 

This also corresponds to the percentage elapsed of a day,

> i.e. 42.07% or 0.42070 of a day = \
> \
> 4 decimal hours \
> 20 decimal minutes \
> 70 decimal seconds \
> _(~10:05:48 in standard metric time.)_

The conversion to standard time is as follows:

>1 decimal second = 0.864 seconds \
>1 decimal minute = 1.44 minutes \
>1 decimal hour = 2.4 hours 

## Date

There is not a well-established idea of "decimal date", so here this is a straightforward representation of the date as a percentage of the elapsed year, with the current year prefixed to it. A year is split into 1 months, with each month split into 100 "_days_", giving each year 1000 "_days_". \
\
This system is a lot more messy than the decimal time above. Where the decimal time is a measure of calculating a fraction of a standard day, this "decimal date" system is a measure of calculating a fraction of a standard year. As such, a day on the decimal clock doesn't correspond to a "_decimal day_":
>~2.74 "_decimal days_" = 1 standard day\
>1 "_decimal day_"  = 8 hour 45 min 36 sec

An ~8-9 hour period 

A "month" is a little simpler, but also doesn't sync with the end of standard day:
>1 "_decimal month_" = 36.5 standard days

There's also the added wrinkle of a leap year. As the "_decimal day_" is a 1/1000 of a year, with an extra day in a leap year, this changes how long a "_decimal day_" is, with fewer "_decimal leap days_" in a normal day.
>~2.73 "decimal leap days" = 1 standard day\
>1 "_decimal leap day_" = 8 hour 47 min 2.4 sec

And a "_decimal leap month_" is slightly longer too:
>1 "_decimal month_" = 36.6 standard days

___

![Principal Skinner, from The Simpsons, smiling with arms folded in front of a "decimal clock" on the wall, showing the numbers 1-10 around the edge of the clock.](img/decimal_skinner.jpg)

*(Though, this isn't "metric time" as Skinner calls it, as [metric time](https://en.wikipedia.org/wiki/Metric_time) is just normal standard time...)*















