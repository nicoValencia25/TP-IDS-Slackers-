package com.tp_ids.hoteles.room

import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.tp_ids.hoteles.R

class RoomViewHolder(view: View) : RecyclerView.ViewHolder(view) {
    private val tvRoomName: TextView = view.findViewById(R.id.tvRoomName)
    private val ivRoom: ImageView = view.findViewById(R.id.ivRoom)
    private val tvRoomDescription: TextView = view.findViewById(R.id.tvRoomDescription)
    private val tvGuestsRoom: TextView = view.findViewById(R.id.tvGuestsRoom)
    private val tvPriceAdultRoom: TextView = view.findViewById(R.id.tvPriceAdultRoom)
    private val tvPriceChildrenRoom: TextView = view.findViewById(R.id.tvPriceChildrenRoom)
    private val btnRoom: Button = view.findViewById(R.id.btnRoom)

    fun render(room: Room) {
        tvRoomName.text = room.name
        // TODO poner la imagen
        tvRoomDescription.text = room.description
        tvGuestsRoom.text = "Huespedes: ${room.guests.toString()}"
        tvPriceAdultRoom.text = "Precio Adultos: \$${room.priceAdult.toString()}"
        tvPriceChildrenRoom.text = "Precio Niños: \$${room.priceChildren.toString()}"
    }
}