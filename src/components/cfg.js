import React, { Component } from "react"

class CFG extends Component {

  constructor(props){
    super(props);
    this.state = {
      accept: false,
      cfg_map: {},
      string: ''
    }
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    this.fetchData()
  }

  handleChange(event) {
    this.setState({string: event.target.value})
  }


  fetchData = () => {
    fetch("https://csmathtools.herokuapp.com/api/cfg/", {method: "POST",
      body: JSON.stringify({accept: this.accept,
        cfg_map: this.cfg_map, string: this.string})})
      .then((data) => {
        this.setState({accept: data.accept, cfg_map: data.cfg_map, string: data.string})
      })
  }

  render (){

    return (
      <div>
        <form onSubmit={this.fetchData}>
          <label>
            String:
            <input type="text" value={this.state.string} onChange={this.handleChange} />        </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    )
  }

}

export default CFG