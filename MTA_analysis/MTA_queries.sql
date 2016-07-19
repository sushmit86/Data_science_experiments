####################################################################################################################################
############################################Analysis Rough queries  starts ############################################
#########################################################################################################################

# query to get the Average time and No of trains per day 
 ##for weekday


select 
trips.route_id 'ROUTE ID',
trips.trip_headsign 'DESTINATION', 
##routes.route_long_name 'ROUTE NAME',

count(trips.trip_id) 'No of trips per day' ,
round(Avg(time_dur.duration),0) 'Avg Time in minutes'
from trips
left join routes
on trips.route_id = routes.route_id

left join(
select trip_id,
TIMESTAMPDIFF(MINUTE,min(arrival_time),
 max(arrival_time)) duration
from
stop_times
group by 1) time_dur
on trips.trip_id = time_dur.trip_id
where service_id
in
(

select service_id
from calendar
where (saturday !=1 and sunday !=1))

group by 1,2;


# query to get the Average time and No of trains per day 
 ##for saturday
 select 
trips.route_id 'ROUTE ID',
trips.trip_headsign 'DESTINATION', 
##routes.route_long_name 'ROUTE NAME',
count(trips.trip_id) 'No of trips per day' ,
round(Avg(time_dur.duration),0) 'Avg Time in minutes'
from trips
left join routes
on trips.route_id = routes.route_id

left join(
select trip_id,
TIMESTAMPDIFF(MINUTE,min(arrival_time),
 max(arrival_time)) duration
from
stop_times
group by 1) time_dur
on trips.trip_id = time_dur.trip_id

where service_id 
in
(
select service_id
from calendar
where (saturday =1))

group by 1,2
;



# query to get the Average time and No of trains per day 
 ##for sunday
select 
trips.route_id 'ROUTE ID',
trips.trip_headsign 'DESTINATION', 
##routes.route_long_name 'ROUTE NAME',
count(trips.trip_id) 'No of trips per day' ,
round(Avg(time_dur.duration),0) 'Avg Time in minutes'
from trips
left join routes
on trips.route_id = routes.route_id

left join(
select trip_id,
TIMESTAMPDIFF(MINUTE,min(arrival_time),
 max(arrival_time)) duration
from
stop_times
group by 1) time_dur
on trips.trip_id = time_dur.trip_id

where service_id 
in
(
select service_id
from calendar
where (sunday =1))

group by 1,2
;


####################################################################################################################################
############################################Analysis Rough queries  ends ############################################
#########################################################################################################################



####################################################################################################################################
############################################Tableau queries starts ############################################
#########################################################################################################################

 # Queries for No of round trips and Average time Weekday
select 
concat_ws('_',trips.route_id ,routes.route_long_name) 'ROUTE ID_NAME',

count(trips.trip_id) 'No of trips per day' ,
round(Avg(time_dur.duration),0) 'Avg Time in minutes'
from trips
left join routes
on trips.route_id = routes.route_id

left join(
select trip_id,
TIMESTAMPDIFF(MINUTE,min(arrival_time),
 max(arrival_time)) duration
from
stop_times
group by 1) time_dur
on trips.trip_id = time_dur.trip_id
where service_id
in
(

select service_id
from calendar
where (saturday !=1 and sunday !=1))

group by 1;

 # Queries for No of round trips and Average time Saturday


select 
concat_ws('_',trips.route_id ,routes.route_long_name) 'ROUTE ID_NAME',

count(trips.trip_id) 'No of trips per day' ,
round(Avg(time_dur.duration),0) 'Avg Time in minutes'
from trips
left join routes
on trips.route_id = routes.route_id

left join(
select trip_id,
TIMESTAMPDIFF(MINUTE,min(arrival_time),
 max(arrival_time)) duration
from
stop_times
group by 1) time_dur
on trips.trip_id = time_dur.trip_id
where service_id
in
(

select service_id
from calendar
where (saturday =1))

group by 1;


# Queries for No of round trips and Average time Sunday


select 
concat_ws('_',trips.route_id ,routes.route_long_name) 'ROUTE ID_NAME',

count(trips.trip_id) 'No of trips per day' ,
round(Avg(time_dur.duration),0) 'Avg Time in minutes'
from trips
left join routes
on trips.route_id = routes.route_id

left join(
select trip_id,
TIMESTAMPDIFF(MINUTE,min(arrival_time),
 max(arrival_time)) duration
from
stop_times
group by 1) time_dur
on trips.trip_id = time_dur.trip_id
where service_id
in
(

select service_id
from calendar
where (sunday =1))

group by 1;


# Traffic over period of a  day for weekday

select 

case when 
((TIMESTAMPDIFF
(SECOND,arrival_time,MAKETIME(23,59,59))) < 0)
then

 
HOUR(TIMEDIFF(arrival_time,'24:00:00'))
else
HOUR(arrival_time) end as Hour_day,

count(distinct(stop_times.trip_id)) as 'No of Trains Operating'

from stop_times
where trip_id in

(select distinct(trip_id )
from trips
left join calendar
on trips.service_id = calendar.service_id
 where (calendar.saturday !=1 and calendar.sunday !=1)) 

group by 1;


# Traffic over period of a  day for Saturday

select 

case when 
((TIMESTAMPDIFF
(SECOND,arrival_time,MAKETIME(23,59,59))) < 0)
then

 
HOUR(TIMEDIFF(arrival_time,'24:00:00'))
else
HOUR(arrival_time) end as Hour_day,

count(distinct(stop_times.trip_id)) as 'No of Trains Operating'

from stop_times
where trip_id in

(select distinct(trip_id )
from trips
left join calendar
on trips.service_id = calendar.service_id
 where (calendar.saturday =1)) 

group by 1;

# Traffic over period of a  day for Saturday

select 

case when 
((TIMESTAMPDIFF
(SECOND,arrival_time,MAKETIME(23,59,59))) < 0)
then

 
HOUR(TIMEDIFF(arrival_time,'24:00:00'))
else
HOUR(arrival_time) end as Hour_day,

count(distinct(stop_times.trip_id)) as 'No of Trains Operating'

from stop_times
where trip_id in

(select distinct(trip_id )
from trips
left join calendar
on trips.service_id = calendar.service_id
 where (calendar.sunday =1)) 

group by 1;


# Traffic over period of a  day for Sunday

select 

case when 
((TIMESTAMPDIFF
(SECOND,arrival_time,MAKETIME(23,59,59))) < 0)
then

 
HOUR(TIMEDIFF(arrival_time,'24:00:00'))
else
HOUR(arrival_time) end as Hour_day,

count(distinct(stop_times.trip_id)) as 'No of Trains Operating'

from stop_times
where trip_id in

(select distinct(trip_id )
from trips
left join calendar
on trips.service_id = calendar.service_id
 where (calendar.Sunday =1)) 

group by 1;

# Busiest Station Weekday

select 
stops_temp.parent_stop_id as 'PARENT STOP ID',
stops_temp.stop_name as 'STOP NAME',
count(distinct(stop_times.trip_id)) as 'No of Trains stopping'
from 
stop_times
left join 
(
select stop_id,
stop_name,
case when stops.parent_station  = ''
then stops.stop_id
else stops.parent_station end as parent_stop_id
 from
stops) stops_temp
on stop_times.stop_id = stops_temp.stop_id
where trip_id in

(select distinct(trip_id )
from trips
left join calendar
on trips.service_id = calendar.service_id
 where (calendar.saturday !=1 and calendar.sunday !=1)) 

group by 1,2
;


# Busiest Station Saturday
select 
stops_temp.parent_stop_id as 'PARENT STOP ID',
stops_temp.stop_name as 'STOP NAME',
count(distinct(stop_times.trip_id)) as 'No of Trains stopping'
from 
stop_times
left join 
(
select stop_id,
stop_name,
case when stops.parent_station  = ''
then stops.stop_id
else stops.parent_station end as parent_stop_id
 from
stops) stops_temp
on stop_times.stop_id = stops_temp.stop_id
where trip_id in

(select distinct(trip_id )
from trips
left join calendar
on trips.service_id = calendar.service_id
 where (calendar.saturday=1)) 

group by 1,2
;


# Busiest Station Sunday
select 
stops_temp.parent_stop_id as 'PARENT STOP ID',
stops_temp.stop_name as 'STOP NAME',
count(distinct(stop_times.trip_id)) as 'No of Trains stopping'
from 
stop_times
left join 
(
select stop_id,
stop_name,
case when stops.parent_station  = ''
then stops.stop_id
else stops.parent_station end as parent_stop_id
 from
stops) stops_temp
on stop_times.stop_id = stops_temp.stop_id
where trip_id in

(select distinct(trip_id )
from trips
left join calendar
on trips.service_id = calendar.service_id
 where (calendar.sunday=1)) 

group by 1,2
;


###################  Routes Changed  ###########


select 
#calendar_dates.service_id,
(calendar_dates.date) as 'DATE',
group_concat(distinct trips.route_id SEPARATOR ',') as 'ROUTES EXCEPTION'
from calendar_dates
left join trips
on calendar_dates.service_id = trips.service_id
where calendar_dates.exception_type = 2
group by 1
;



select 
#calendar_dates.service_id,
date(calendar_dates.date) as 'DATE',
group_concat(distinct trips.route_id SEPARATOR ',') as 'ROUTES EXCEPTION'
from calendar_dates
left join trips
on calendar_dates.service_id = trips.service_id
where calendar_dates.exception_type = 1
group by 1
;


############ Transfer table ############

select 

t1.`From Stop Name`,
 t1.`To Stop Name`,
 t1.min_transfer_time
from
(

select transfers.*,
stops.stop_name as 'From Stop Name',
(select stops.stop_name from stops where stops.stop_id = transfers.to_stop_id) as 'To Stop Name'
from transfers

left join stops
on stops.stop_id = from_stop_id) t1
where t1.`From Stop Name`!=  t1.`To Stop Name`






####################################################################################################################################
############################################Tableau queries ends ############################################
#########################################################################################################################














 
 


