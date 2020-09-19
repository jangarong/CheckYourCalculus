import React from "react";
import { Link } from "gatsby";
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';
import AppMap from './appmap.js';

class Apps extends React.Component{
  constructor() {
    super();
    this.state = {
      width: 0,
      box_xs: 4
    };
  }
  // event listener for window size (to determine whether user is in mobile or not).
  componentDidMount() {
    this.handleWindowSizeChange()
    window.addEventListener('resize', this.handleWindowSizeChange);
  }
  componentWillUnmount() {
    window.removeEventListener('resize', this.handleWindowSizeChange);
  }
  handleWindowSizeChange = () => {
    this.setState({ width: window.innerWidth });
  };
  render() {
    const {width} = this.state;
    const isMobile = width <= 1280;
    const paperStyling = {
      height: "100%",
      padding: 30,
      color: 'white',
      backgroundColor: '#3b3b3b'
    }
    if (isMobile){
      this.box_xs = 12;
    } else {
      this.box_xs = 4;
    }
    return (
      <Grid container spacing={3} justify={'space-evenly'}>
          {AppMap.map((module) => (
            <Grid item xs={this.box_xs}>
              <Paper style={paperStyling} elevation={4} align={'left'}>
                <h2>{module.title}</h2>
                <p>{module.desc}</p>
                <div align={'right'}>
                  <Link to={module.link}>
                    <Button color="secondary">Enter</Button>
                  </Link>
                </div>
              </Paper>
            </Grid>
          ))
          }
      </Grid>
    );
  }
}

export default Apps
