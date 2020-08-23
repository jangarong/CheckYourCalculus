import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, Button, View, TouchableOpacity } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Camera } from 'expo-camera';
import { FontAwesome } from '@expo/vector-icons';
import TouchableScale from 'react-native-touchable-scale';
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';
import * as MediaLibrary from 'expo-media-library';

// To upload equation snippets to an S3 bucket
import { RNS3 } from 'react-native-aws3';
import { keys } from './keys.js';

const config = {
  bucket: 'assets-vjk',
  keyPrefix: 'snippets/',
  region: 'ca-central-1',
  accessKey: keys.s3ID,
  secretKey: keys.s3Secret,
}


// Generate a unique id string to name files uploaded to the S3 bucket
function makeid(length) {
  var result = '';
  var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text style={{ fontSize: 30 }}>This is the home screen!</Text>

      <TouchableScale onPress={() => navigation.navigate('MyModal')} >
        <FontAwesome name="camera" style={{ color: "red", fontSize: 40 }} />
      </TouchableScale>
    </View >
  );
}

function ModalScreen({ navigation }) {
  const [hasPermission, setHasPermission] = React.useState(null);
  const [cameraRollPermissions, setCameraRollPermissions] = React.useState(null);
  const [type, setType] = React.useState(Camera.Constants.Type.back);
  const [snippet, setSnippet] = React.useState({
    "height": 1,
    "uri": "",
    "width": 1,
  });
  // The latex code to be rendered
  const [latex, setLatex] = React.useState('\\text{Type your } \\LaTeX \\text{ code or drag/drop an image below! }');

  // Where to access the image to send to the OCR API
  const [imageURL, setImageURL] = React.useState("");
  const [image, setImage] = React.useState({});

  const cameraRef = React.useRef();

  const takePicture = async () => {
    if (cameraRef) {



      // Take a photo and return its information
      setImage(await cameraRef.current.takePictureAsync());

      console.log(typeof image);


    };

  }

  const uploadS3 = () => {
    // Photos taken by the camera are in jpg format, construct a random filename
    const fileName = `snippet_${makeid(8)}.jpg`;

    // Construct a file object from the photo URI
    let file = {
      uri: image.uri,
      name: fileName,
      type: "image/jpg"
    };

    // Upload the snippet to an S3 bucket with a randomized filename
    RNS3.put(file, config).then(res => {
      if (res.status !== 201)
        throw new Error("Failed to upload image to S3");


      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'app_id': keys.email, 'app_key': keys.mathpix },
        body: JSON.stringify({ "src": `${res.body.location}` })
      };

      fetch('https://api.mathpix.com/v3/text', requestOptions)
        .then(response => response.json())
        .then(data => {
          console.log(data);
          setLatex(JSON.parse(JSON.stringify(data.latex_styled)))
          console.log(latex);
        })
        .catch((err) => {
          console.log("Failed to OCR, " + err);
        });


      console.log(res.body);
    })
  };

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
    });
  }

  React.useEffect(() => {
    (async () => {
      const { status } = await Camera.requestPermissionsAsync();
      // Camera roll Permission 
      if (Platform.OS === 'ios') {
        const { cameraRollStatus } = await Permissions.askAsync(Permissions.CAMERA_ROLL);
        if (cameraRollStatus !== 'granted') {
          alert('Sorry, we need camera roll permissions to make this work!');
        }
      }

      setCameraRollPermissions(cameraRollPermissions === 'granted')
      setHasPermission(status === 'granted');
    })();
  }, []);

  if (hasPermission === null) {
    return <View />;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }
  return (
    <View style={{ flex: 1 }}>
      <Camera style={{ flex: 1 }} type={type} ref={cameraRef}>
        <View
          style={{
            flex: 1,
            backgroundColor: 'transparent',
            flexDirection: 'row',
          }}>
          <TouchableOpacity
            style={{
              flex: 0.1,
              alignSelf: 'flex-end',
              alignItems: 'center',
            }}
            onPress={() => {
              setType(
                type === Camera.Constants.Type.back
                  ? Camera.Constants.Type.front
                  : Camera.Constants.Type.back
              );
            }}>
            <Text style={{ fontSize: 18, marginBottom: 10, color: 'white' }}> Flip </Text>
          </TouchableOpacity>
        </View>
      </Camera>
      <Button onPress={() => {
        takePicture();
        uploadS3();
      }}

        title="Take photo" />
      <Button onPress={() => navigation.goBack()} title="Dismiss" />
    </View>
  );
}

const MainStack = createStackNavigator();
const RootStack = createStackNavigator();

function MainStackScreen() {
  return (
    <MainStack.Navigator>
      <MainStack.Screen name="Home" component={HomeScreen} />
    </MainStack.Navigator>
  );
}

function App() {
  return (
    <NavigationContainer>
      <RootStack.Navigator mode="modal" headerMode="none">
        <RootStack.Screen name="Main" component={MainStackScreen} />
        <RootStack.Screen name="MyModal" component={ModalScreen} />
      </RootStack.Navigator>
    </NavigationContainer>
  );
}

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
