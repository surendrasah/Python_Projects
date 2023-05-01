--
-- PostgreSQL database dump
--

-- Dumped from database version 12.14 (Ubuntu 12.14-1.pgdg20.04+1)
-- Dumped by pg_dump version 12.14 (Ubuntu 12.14-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cocktails; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cocktails (
    name text NOT NULL,
    ingredients text[],
    instructions text,
    glass_type text
);


ALTER TABLE public.cocktails OWNER TO postgres;

--
-- Data for Name: cocktails; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cocktails (name, ingredients, instructions, glass_type) FROM stdin;
Caipirinha	{Cachaca,"Lime juice"}	Place lime and sugar into old fashioned glass and muddle (mash the two ingredients together using a muddler or a wooden spoon). Fill the glass with ice and add the Cachaça.	Old-fashioned glass
Margarita	{Tequila,"Triple sec",Cointreau}	Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.	Cocktail glass
Pina Colada	{"White rum","Coconut cream","Pineapple juice"}	Mix with crushed ice in blender until smooth. Pour into chilled glass, garnish and serve.	Collins glass
Long Island Iced Tea	{Vodka,Gin,"White Rum",Tequila,"Triple sec","Lemon juice",Cola}	Mix all contents in a highball glass and sitr gently. Add dash of Coca-Cola for the coloring and garnish with lemon or lime twist.	Highball glass
Daiquiri	{"White rum","Lime juice"}	Pour all ingredients into shaker with ice cubes. Shake well. Strain in chilled cocktail glass.	Cocktail glass
Moscow Mule	{Vodka,"Ginger beer","Lime juice"}	Combine vodka and ginger beer in a highball glass filled with ice. Add lime juice. Stir gently. Garnish.	Copper Mug
Gin Mule	{Gin,"Ginger beer","Lime juice"}		
Aperol Spritz	{Prosecco,Aperol,Soda}	Put a couple of cubes of ice into 2 glasses and add a 50 ml measure of Aperol to each. Divide the prosecco between the glasses and then top up with soda, if you like.	Wine Glass
White Russian	{"Coffee liqueur",Vodka}	Pour vodka and coffee liqueur over ice cubes in an old-fashioned glass. Fill with light cream and serve.	Old-fashioned glass
Gin Fizz	{Gin,Soda,"Lemon juice"}	Shake all ingredients with ice cubes, except soda water. Pour into glass. Top with soda water.	Highball glass
Cosmopolitan	{Vodka,Cointreau,"Cranberry juice"}	Add all ingredients into cocktail shaker filled with ice. Shake well and double strain into large cocktail glass. Garnish with lime wheel.	Cocktail glass
Mojito	{"Lime juice","White rum",Soda}	Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.	Highball glass
Mai Tai	{"White rum","Dark rum","Orange Curacao","Almond syrup","Lime juice"}	Shake all ingredients with ice. Strain into glass. Garnish and serve with straw.	Collins glass
\.


--
-- Name: cocktails cocktails_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cocktails
    ADD CONSTRAINT cocktails_pkey PRIMARY KEY (name);


--
-- PostgreSQL database dump complete
--

