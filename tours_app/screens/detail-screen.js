import { useNavigation, useRoute } from "@react-navigation/native"
import { useLayoutEffect } from "react"
import {View, Text, StyleSheet} from "react-native"
import {HeaderBackButton} from "@react-navigation/elements"


const DetailScreen = () => {
    const route = useRoute()
    const{eventId, name, description} = route.params
    const navigation = useNavigation()

    useLayoutEffect(()=> {
        navigation.setOptions({
            headerTitle: "new title",
            headerLeft: () => (
                <HeaderBackButton
                    tintColor="white"
                    onPress={()=> navigation.goBack()}
                />
            ) 
        })
    }, [])

    return (
        <View style={styles.screen}>
            <Text style={{fontSize: 20}}>This is the Event Detail Screen for {eventId}</Text>
            <Text style={{fontSize: 20}}>{name}</Text>
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