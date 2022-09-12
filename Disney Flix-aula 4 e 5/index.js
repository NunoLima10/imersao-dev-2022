const movies_box = document.getElementById('movies_box')
const find_input = document.getElementById('find_input')
const movies = [
    "A Bela e A Fera",
    "A pequena Seriea",
    "Branca de neve",
    "Rei  Leão",
    "A Princesa e o Sapo",
    "Aladdin",
    "Cinderela",
    "Lilo & Stitch",
    "Mulan",
    "Pinóquio",
]

function GenerateMovieCard(name){
    var movie_card = document.createElement('DIV')
    var movie_img = document.createElement('IMG')
    var movie_name = document.createElement('P')

    movie_name.innerText = name
    movie_img.src = "assets/" + name + ".jpg"

    movie_card.classList.add("movie_card")
    movie_img.classList.add("movie_img")
    movie_name.classList.add("movie_name")
    movie_card.append(movie_img)
    movie_card.append(movie_name)
    return movie_card
}

function GenerateMovieList(movie_list){
    for(var i = 0; i< movie_list.length ; i++){
     movie_card = GenerateMovieCard(movie_list[i])
        movies_box.append(movie_card)
    }

}

function FindMoviesByName(name){
    var movie_list = []
    for(var i=0 ; i<movies.length ; i++){
        if(!(movies[i].search(name))){
            movie_list.push(movies[i])
        }
    }
    return movie_list
}

function find(){
    movie_name = find_input.value
    movies_box.innerHTML = ""
    if (movie_name.length==0){
        GenerateMovieList(movies)
        return
    }
    movie_list = FindMoviesByName(movie_name)
    GenerateMovieList(movie_list)
}
GenerateMovieList(movies)


