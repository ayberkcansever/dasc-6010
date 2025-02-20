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

create unique index kline_btc_moment_uindex on public.kline_btc (moment);
create unique index kline_ada_moment_uindex on public.kline_ada (moment);
create unique index kline_xrp_moment_uindex on public.kline_xrp (moment);
create unique index kline_sol_moment_uindex on public.kline_sol (moment);
create unique index kline_eth_moment_uindex on public.kline_eth (moment);
create unique index kline_bnb_moment_uindex on public.kline_bnb (moment);