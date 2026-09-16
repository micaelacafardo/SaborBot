def _mostrar_resultados_con_detalle(resultados):
    if not resultados:
        print("\n🔍 No se encontraron recetas.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    for idx, receta in enumerate(resultados, 1):
        print(f"{idx}. {receta.nombre} ({receta.categoria}) - ⭐{receta.valoracion}")

    seleccion = input("\nVer detalle de una receta (número, Enter para omitir): ").strip()
    if seleccion.isdigit():
        num = int(seleccion)
        if 1 <= num <= len(resultados):
            r = resultados[num - 1]
            print("\n" + "~" * 30)
            print(f"📖 {r.nombre.upper()}")
            print(f"   • Categoría: {r.categoria}")
            print(f"   • Dificultad: {r.dificultad}")
            print(f"   • Valoración: {r.valoracion}/10")
            print(f"   • Tiempo: {r.tiempo_min} min")
            print(f"   • Ingredientes: {', '.join(r.ingredientes)}")
            print("~" * 30)
            
            # 🛑 ESTO ES LO QUE FRENABA EL FLUJO:
            input("\nPresioná [Enter] para volver al menú principal...")
        else:
            print("❌ Número de receta fuera de rango.")
            input("\nPresioná [Enter] para continuar...")
            