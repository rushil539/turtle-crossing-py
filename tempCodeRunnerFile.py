    car_left = cars.xcor() - 20   
        car_right = cars.xcor() + 2
        car_top = cars.ycor() + 10    
        car_bottom = cars.ycor() - 10 
        player_x = player.xcor()
        player_y = player.ycor()
        if car_left < player_x < car_right and car_bottom < player_y < car_top: