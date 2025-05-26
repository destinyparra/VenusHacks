# Zot Spot
**Live site: https://venushacks-1.onrender.com/**

## Inspiration
We were inspired by the stress and uncertainty students often face when trying to manage their periods on campus. Even though some bathrooms have products available, it is unclear which ones, whether the products are free, or if they are currently stocked. This lack of visibility and access can create shame, discomfort, and inconvenience, especially for women and menstruating students who are moving between long classes, jobs, and commutes. Zot Spot was born out of a desire to make period care on campus more accessible, visible, and reliable.

## What it does
Zot Spot is a web-based tool that helps students locate bathrooms on the UC Irvine campus that offer free period products. It displays an interactive map with real-time availability markers. Users can view bathroom locations, check stock levels for pads and tampons, and report when items are low or out of stock. The application also uses browser location services to help users find the nearest stocked bathroom and estimate walking time and distance.

## How we built it
We built Zot Spot using **Python and micro web framework Flask** for the backend and **Leaflet.js** for the interactive campus map. Our data on bathrooms is stored in a SQLite database using Python, organized by building, floor, and room number. Each entry includes details like product availability for pads and tampons, whether the location is free, and when it was last updated.

For the frontend, we used **HTML, CSS,** and **JavaScript**. We implemented geolocation so that users can see their location on the map, and we calculate both the distance to each bathroom and an estimated walking time based on a standard walking pace. This allows users to make quick, informed decisions without the need for step-by-step routing or external APIs.

We also created a reporting system that lets users submit updates when a product is low or out of stock. These updates are timestamped and reflected in both the map view and the list view. The application is designed to be accessible, responsive, and easy to use across desktop and mobile devices.

## Challenges we ran into
We ran into several challenges during development. We had to manually gather coordinates and floor-level data for dozens of bathrooms on campus, which was time-consuming and required careful formatting. Leaflet’s built-in routing options did not suit our needs for campus footpaths, so we focused on calculating and displaying walking distances and times instead. Balancing design clarity with information density on smaller screens also required multiple interface revisions and testing across devices.

## Accomplishments that we're proud of
We are proud that Zot Spot is a usable and helpful tool that addresses a real problem experienced by many students. We built a working map interface, allowed live reporting, and designed an intuitive layout with care and accessibility in mind. Zot Spot is not just a tech demo. It empowers users to find what they need without stress or shame. We are proud of the way we thought through user experience, inclusion, and how to make a technical solution feel supportive and thoughtful.

## What we learned
We learned how to combine frontend mapping technologies with a backend reporting system in a meaningful way. We gained experience working with Flask, Leaflet, and geolocation tools, while also learning how to structure and manage location data. Most importantly, we learned how to approach a sensitive but important topic like menstrual health with care, technical creativity, and empathy. Zot Spot taught us how to build with impact and intention.

## What's next for Zot Spot
Our next step is to connect Zot Spot with UCI wellness services or janitorial teams so that it can become part of a long-term restocking solution. We also plan to add features such as gender-neutral bathroom filtering, anonymous reporting, and support for multiple product types. We hope to create a scalable backend to bring Zot Spot to other campuses and build an analytics dashboard that helps monitor product availability and refill frequency. The goal is simple. No student should have to stress about finding a pad or tampon when they need one.

