// Create the blue square that will be clicked to show/hide red squares
function showApplicationSetting(content) {
    const blueSquare = content.append("rect")
        .attr("class", "rectangle")
        .attr("x", 50)
        .attr("y", 25)
        .attr("width", 100)
        .attr("height", 50)
        .on("mouseenter", function () {
            d3.select(this).attr("stroke", "grey"); // Change outline color on hover
        })
        .on("mouseleave", function () {
            d3.select(this).attr("stroke", "black"); // Revert outline color on mouse leave
        }).on("click", toggleRedSquares);
        content.append("text")
        .attr("class", "text-high")
        .attr("x", 100)
        .attr("y", 55)
        .attr("text-anchor", "middle")
        .text("Love");


    // .attr("class", "blue-square")
    // .attr("x", 50)
    // .attr("y", 50)
    // .attr("width", 50)
    // .attr("height", 50)
    // .on("click", toggleRedSquares);
    //
    // content.append("text")
    //       .attr("x", 60) // Adjust text position
    //       .attr("y", 60) // Adjust text position
    //       .attr("text-anchor", "middle")
    //       .attr("fill", "black")
    //       .text("Text 1");

    //   // Arrays to store elements for red, green, yellow, and orange shapes and curves
      const redSquares = [];
      const greenSquares = [];
      const yellowSquares = [];
      const orangeSquares = [];
      const greyCurves = [];
      const pinkCurves = [];
      const blackCurves = [];
      const purpleCurves = [];
    //
      // Loop to create red squares, green squares, curves, and handle click events
      for (let i = 0; i < 3; i++) {
        // Create red squares and grey curves between blue and red squares
        const redSquare = content.append("rect")
                .attr("class", "red-square")
                .attr("x", 120)
                .attr("y", 50 + i * 100)
                .attr("width", 50)
                .attr("height", 50)
                .on("click", function () {
            if (i === 0) {
                toggleGreenSquares(0);
            }
        });

        redSquares.push(redSquare);

        if (i === 0) {
        content.append("text")
            .attr("x", 140) // Adjust the x position as needed
            .attr("y", 80) // Adjust the y position as needed
            .attr("class", "text-inside")
            .attr("text-anchor", "middle")
            .text("Love")
            .style("display", "none");
    }
         if (i === 1) {
        content.append("text")
            .attr("x", 140) // Adjust the x position as needed
            .attr("y", 180) // Adjust the y position as needed
            .attr("class", "text-inside")
            .attr("text-anchor", "middle")
            .text("Love")
            .style("display", "none");
    }

         if (i === 2) {
        content.append("text")
            .attr("x", 140) // Adjust the x position as needed
            .attr("y", 280) // Adjust the y position as needed
            .attr("class", "text-inside")
            .attr("text-anchor", "middle")
            .text("Love")
            .style("display", "none");
    }

        const greyCurve = content.append("path")
                .attr("class", "grey-curve")
                .attr("d", `M100,75 Q120,${75 + i * 100} 120,${75 + i * 100}`)
                .style("display", "none");
        greyCurves.push(greyCurve);

        // Create green squares and pink curves between red and green squares
        const greenSquare = content.append("rect")
                .attr("class", "green-square")
                .attr("x", 190)
                .attr("y", 50 + i * 100)
                .attr("width", 30)
                .attr("height", 30)
                .on("click", function () {
                  toggleYellowSquares(i);
                });
        greenSquares.push(greenSquare);

        const pinkCurve = content.append("path")
                .attr("class", "pink-curve")
                .attr("d", `M170,75 Q170,${75 + i * 100} 190,${75 + i * 100}`)
                .style("display", "none");
        pinkCurves.push(pinkCurve);

        // Create yellow squares, orange squares, purple, and black curves between green and yellow squares
        const yellowSquare1 = content.append("rect")
                .attr("class", "yellow-square")
                .attr("x", 230)
                .attr("y", 60 + i * 100)
                .attr("width", 20)
                .attr("height", 20)
                .on("click", function () {
                  toggleOrangeSquares(i);
                })
                .style("display", "none");

        const yellowSquare2 = content.append("rect")
                .attr("class", "yellow-square")
                .attr("x", 230)
                .attr("y", 90 + i * 100)
                .attr("width", 20)
                .attr("height", 20)
                .on("click", function () {
                  toggleOrangeSquares(i);
                })
                .style("display", "none");
        yellowSquares.push([yellowSquare1, yellowSquare2]);

        const purpleCurve = content.append("path")
                .attr("class", "purple-curve")
                .attr("d", `M220,70 Q240,${70 + i * 100} 220,${70 + i * 100}`)
                .style("display", "none");
        purpleCurves.push(purpleCurve);

        const blackCurve1 = content.append("path")
                .attr("class", "black-curve")
                .attr("d", `M215,70 Q225,${70 + i * 100} 235,${70 + i * 100}`)
                .style("display", "none");

        // const blackCurve2 = svg.append("path")
        //   .attr("class", "black-curve")
        //   .attr("d", `M215,90 Q225,${90 + i * 100} 235,${90 + i * 100}`)
        //   .style("display", "none");
        blackCurves.push([blackCurve1,]);

        const orangeSquare1 = content.append("rect")
                .attr("class", "orange-square")
                .attr("x", 270)
                .attr("y", 65 + i * 100)
                .attr("width", 15)
                .attr("height", 15)
                .style("display", "none");

        const orangeSquare2 = content.append("rect")
                .attr("class", "orange-square")
                .attr("x", 270)
                .attr("y", 90 + i * 100)
                .attr("width", 15)
                .attr("height", 15)
                .style("display", "none");
        orangeSquares.push([orangeSquare1, orangeSquare2]);
      }


      let redSquaresVisible = false;

      // Function to toggle visibility of red squares and associated grey curves
      // Function to toggle visibility of red squares and associated grey curves


      // // Function to toggle text content inside red squares
      // function toggleTextContent(squareIndex) {
      //   // Different text content for each red square
      //   const textContents = ["First Text", "Second Text", "Third Text"];
      //
      //   const redSquare = d3.select(`#redSquare${squareIndex}`);
      //   const existingText = redSquare.select("text");
      //
      //   if (existingText.empty()) {
      //     redSquare.append("text")
      //             .text(textContents[squareIndex - 1]) // Index adjusted for the array
      //             .attr("x", 120 + 50 / 2) // X position in the middle of the square
      //             .attr("y", 50 + (squareIndex - 1) * 100 + 50 / 2) // Y position in the middle of the square
      //             .attr("dy", "0.35em"); // Vertical alignment adjustment
      //   } else {
      //     existingText.remove();
      //   }
      // }

      function toggleRedSquares() {
        // Toggle visibility of red squares and grey curves
        redSquaresVisible = !redSquaresVisible;

        redSquares.forEach((square, index) => {
          square.style("display", redSquaresVisible ? "block" : "none");
        const text = content.selectAll(".text-inside").filter((d, i) => i === index);
        text.style("display", redSquaresVisible ? "block" : "none");
        greyCurves.forEach(curve => {
          curve.style("display", redSquaresVisible ? "block" : "none");
        });

        if (!redSquaresVisible) {
          greenSquares.forEach(square => square.style("display", "none"));
          yellowSquares.forEach(squares => squares.forEach(square => square.style("display", "none")));
          orangeSquares.forEach(squares => squares.forEach(square => square.style("display", "none")));
          pinkCurves.forEach(curve => curve.style("display", "none"));
          blackCurves.forEach(curve => curve.forEach(line => line.style("display", "none")));
          purpleCurves.forEach(curve => curve.style("display", "none"));
        }
      });
    }

    // Function to toggle visibility of green squares and associated pink curves
    function toggleGreenSquares(index) {
      // Toggle visibility of green squares and pink curves
      const greenSquareToShow = greenSquares[index];
      const pinkCurveToShow = pinkCurves[index];

      if (greenSquareToShow && pinkCurveToShow) {
        const displayStyle = greenSquareToShow.style("display");

        greenSquareToShow.style("display", displayStyle === "none" ? "block" : "none");
        pinkCurveToShow.style("display", displayStyle === "none" ? "block" : "none");
        yellowSquares.forEach(squares => squares.forEach(square => square.style("display", "none")));
        orangeSquares.forEach(squares => squares.forEach(square => square.style("display", "none")));
        blackCurves.forEach(curve => curve.forEach(line => line.style("display", "none")));
        purpleCurves.forEach(curve => curve.style("display", "none"));
      }
    }

    // Function to toggle visibility of yellow squares and associated purple curves
    function toggleYellowSquares(index) {
      // Toggle visibility of yellow squares and purple curves
      const yellowSquaresToShow = yellowSquares[index];
      const purpleCurveToShow = purpleCurves[index];

      if (yellowSquaresToShow && purpleCurveToShow) {
        const displayStyle = yellowSquaresToShow[0].style("display");

        yellowSquaresToShow.forEach(square => {
          square.style("display", displayStyle === "none" ? "block" : "none");
        });

        purpleCurveToShow.style("display", displayStyle === "none" ? "block" : "none");
        orangeSquares.forEach(squares => squares.forEach(square => square.style("display", "none")));
        blackCurves.forEach(curve => curve.forEach(line => line.style("display", "none")));

      }
    }

    // Function to toggle visibility of orange squares and associated black curves
    function toggleOrangeSquares(index) {
      // Toggle visibility of orange squares and black curves
      const orangeSquaresToShow = orangeSquares[index];
      const blackCurvesToShow = blackCurves[index];

      if (orangeSquaresToShow && blackCurvesToShow) {
        const displayStyle = orangeSquaresToShow[0].style("display");

        orangeSquaresToShow.forEach(square => {
          square.style("display", displayStyle === "none" ? "block" : "none");
        });

        blackCurvesToShow.forEach(line => {
          line.style("display", displayStyle === "none" ? "block" : "none");
        });

}}}