import React, { Component } from "react"
import { SERVER_URL } from "../../constants"


class Compute extends Component {
  constructor(props) {
    super(props)
    this.state = {
      correct: "no",
      equation: "",
    }
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange(event) {
    //So the page doesn't refresh on change:
    event.preventDefault()
    this.setState({ equation: event.target.value })
  }

  fetchData = (event) => {
    event.preventDefault()
    fetch(SERVER_URL + "/api/compute", {
      method: "POST",
      mode: "cors",
      body: JSON.stringify({
        correct: this.state.correct,
        equation: this.state.equation,
      }),
    }).then(response => response.json())
      .then(data => {
        this.setState({ correct: data.correct, equation: data.equation })
      })
  }

  render() {
    return (
      <div>
        {this.state.correct}
        <form onSubmit={this.fetchData}>
          <label>
            Equation:
            <input
              type="text"
              value={this.state.equation}
              onChange={this.handleChange}
            />{" "}
          </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    )
  }
}

export default Compute
