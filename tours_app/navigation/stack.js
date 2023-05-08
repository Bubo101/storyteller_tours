import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/home-screen';
import DetailScreen from '../screens/detail-screen';

const Stack = createStackNavigator();

export const HomeStack = () => {
    return (
        <Stack.Navigator>
            <Stack.Screen name="Home" component={HomeScreen} />
            <Stack.Screen name="Event" component={DetailScreen} />
        </Stack.Navigator>
    );
}