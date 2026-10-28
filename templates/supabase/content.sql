-- Illustrative PostgreSQL/Supabase migration BODY, not an applied migration.
-- Create the migration with the installed CLI first; use isolated preview only.
-- PUBLIC READ ONLY of published content. No browser write/admin policy supplied.
-- All columns below are intended public when the row is published.
begin;
create table public.products (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique check (length(slug) between 1 and 120),
  name text not null check (length(name) between 1 and 160),
  description text not null default '' check (length(description) <= 10000),
  price_minor integer not null check (price_minor >= 0),
  currency text not null check (currency ~ '^[A-Z]{3}$'),
  category text,
  published boolean not null default false,
  revision integer not null default 1 check (revision > 0),
  deleted_at timestamptz
);
create table public.events (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique check (length(slug) between 1 and 120),
  title text not null check (length(title) between 1 and 160),
  description text not null default '' check (length(description) <= 10000),
  starts_at timestamptz not null,
  ends_at timestamptz not null,
  time_zone text not null,
  location text not null,
  status text not null default 'scheduled' check (status in ('scheduled', 'cancelled', 'postponed')),
  published boolean not null default false,
  revision integer not null default 1 check (revision > 0),
  deleted_at timestamptz,
  check (ends_at > starts_at)
);
alter table public.products enable row level security;
alter table public.events enable row level security;
revoke all on public.products, public.events from anon, authenticated;
grant select on public.products, public.events to anon, authenticated;
create policy "public published products" on public.products
  for select to anon, authenticated using (published and deleted_at is null);
create policy "public published events" on public.events
  for select to anon, authenticated using (published and deleted_at is null);
create index products_published_slug on public.products (slug) where published and deleted_at is null;
create index events_published_start on public.events (starts_at, id) where published and deleted_at is null;
commit;
