import { useRoute } from "@react-navigation/native"
import {View, Text, StyleSheet} from "react-native"

const DetailScreen = () => {
    const route = useRoute()
    const{eventId, title, description} = route.params
    return (
        <View style={styles.screen}>
            <Text style={{fontSize: 20}}>This is the Event Detail Screen for {eventId}</Text>
            <Text style={{fontSize: 20}}>{title}</Text>
            <Text style={{fontSize: 20}}>{description}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    screen: {
        padding: 20,
    }
})

export default DetailScreen