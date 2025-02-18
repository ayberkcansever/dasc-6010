create table public.kline_btc
(
    id                     bigserial,
    moment                 numeric not null,
    high                   numeric,
    open                   numeric,
    low                    numeric,
    close                  numeric,
    volume                 numeric
);

create table public.kline_eth
(
    id                     bigserial,
    moment                 numeric not null,
    high                   numeric,
    open                   numeric,
    low                    numeric,
    close                  numeric,
    volume                 numeric
);


create table public.kline_xrp
(
    id                     bigserial,
    moment                 numeric not null,
    high                   numeric,
    open                   numeric,
    low                    numeric,
    close                  numeric,
    volume                 numeric
);

create table public.kline_bnb
(
    id                     bigserial,
    moment                 numeric not null,
    high                   numeric,
    open                   numeric,
    low                    numeric,
    close                  numeric,
    volume                 numeric
);

create table public.kline_ada
(
    id                     bigserial,
    moment                 numeric not null,
    high                   numeric,
    open                   numeric,
    low                    numeric,
    close                  numeric,
    volume                 numeric
);

create table public.kline_sol
(
    id                     bigserial,
    moment                 numeric not null,
    high                   numeric,
    open                   numeric,
    low                    numeric,
    close                  numeric,
    volume                 numeric
);