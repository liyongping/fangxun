select restricted_units from salestatusquo;

select sum(total_units), sum(sold_units), sum(current_units), sum(restricted_units) from salestatusquo;

select sum(total_units), sum(sold_units), sum(current_units), sum(restricted_units) from salestatusquo
where purpose in ("多层住宅","小高层住宅","高层住宅","别墅","低层住宅","酒店式公寓")

select distinct purpose from salestatusquo;