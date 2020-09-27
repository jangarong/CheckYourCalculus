import React, { Component } from "react"
import { SERVER_URL } from "../../constants"
class CFG extends Component {
  constructor(props) {
    super(props)
    this.state = {
      accept: false,
      cfg_map: {},
      string: "",
    }
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange(event) {
    //So page doesn't reload every time:
    event.preventDefault()
    this.setState({ string: event.target.value })
  }

  fetchData = (event) => {
    event.preventDefault()
    fetch(SERVER_URL + "/api/cfg", {
      method: "POST",
      mode: "cors",
      body: JSON.stringify({
        accept: this.state.accept,
        cfg_map: this.state.cfg_map,
        string: this.state.string,
      }),
    }).then(response => response.json())
      .then(data => {
        //To see response:
        console.log(data)
        this.setState({
          accept: data.accept,
          cfg_map: data.cfg_map,
          string: data.string,
        })
    })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.fetchData}>
          <label>
            String:
            <input
              type="text"
              value={this.state.string}
              onChange={this.handleChange}
            />{" "}
          </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    )
  }
}

export default CFG
