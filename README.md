# MLB-GRAPHICAL-STANDINGS

## Usage

Build
```
chuy build
```

Test
```
chuy build test
```

## What to Expect

This will be a docker image. It will be loaded onto a Raspberry Pi and scheduled to run every Monday morning. It will load up graphical standings for each division, package them up, and then email them to me. Bonus if theres highlighted notes regarding lead changes!

What this will use

- pytest for testing
- Poetry to handle python deps
- docker to handle deployment

Roadmap

O setup basic grpahical standings

O fix clashing colors

O would be really cool if we had chatgpt generate humorous captions

O add pngs of team logos

O test coverage

O docker 

O get logging setup once we have docker in place

