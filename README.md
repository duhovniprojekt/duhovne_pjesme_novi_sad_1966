# Duhovne Pjesme Novi Sad 1966

## Clone this repository and its submodules

```git clone https://github.com/duhovniprojekt/duhovne_pjesme_novi_sad_1966.git```

```git submodule update --init --recursive```

or with a single command

```git clone --recursive https://github.com/duhovniprojekt/duhovne_pjesme_novi_sad_1966.git```


## Add new song repository as a submodule

In the root of the project run:
```git submodule add https://github.com/duhovniprojekt/duhovne_pjesme_novi_sad_1966_001 songs/001```

## Creating a new song repository

- go to https://github.com/duhovniprojekt
- click new
- choose a name in a format like *duhovne_pjesme_novi_sad_1966_NNN* where *NNN* is a number cooresponding to the song
- add this repository as a submodule described above
- cd into new repository
- add folders ```mkdir -p musescore pdf```
- save new musescore project as NNN.mscx (uncompressed) in musescore folder
- export pdf into pdf folder
- commit
- return to the root of the project
- commit new submodule changes

## Edit a song (submodule)

Before you edit a song checkout to master branch using these command sequence:
- `cd songs/001`
- `git checkout master`
- `git pull`
so you wont have errors like `git push origin HEAD:<name-of-remote-branch>`
