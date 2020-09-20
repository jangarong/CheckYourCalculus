import React, { Component } from "react"

class CFG extends Component {
  state = {
    cfgs: []
  }

  componentDidMount() {
    fetch("https://csmathtools.herokuapp.com/api/cfg/")
      .then(res => res.json())
      .then((cfg) => {this.setState({ cfgs: cfg })
      })
  }

  render (){

    const { local_cfgs } = this.state;

    return (
      <div>
        {local_cfgs && local_cfgs.map((cfg) => (
            <div>
              {cfg.string}
            </div>
          ))
        }
      </div>
    )
  }

}

export default CFG