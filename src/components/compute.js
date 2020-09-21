import React, { Component } from "react"

class Compute extends Component {

  constructor(props){
    super(props);
    this.state = {
      correct: "no",
      equation: ""
    }
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    this.fetchData()
  }

  handleChange(event) {
    this.setState({equation: event.target.value})
  }


  fetchData = () => {
    fetch("https://csmathtools.herokuapp.com/api/compute", {method: "POST",
      body: JSON.stringify({correct: this.state.correct, equation: this.state.equation})})
      .then((data) => {
        this.setState({correct: data.correct, equation: data.equation})
      })
  }

  render (){

    return (
      <div>
        {this.state.correct}
        <form onSubmit={this.fetchData}>
          <label>
            Equation:
            <input type="text" value={this.state.equation} onChange={this.handleChange} />        </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    )
  }

}

export default Compute